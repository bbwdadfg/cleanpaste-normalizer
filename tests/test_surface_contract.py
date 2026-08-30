from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))


class SurfaceContractTests(unittest.TestCase):
    def test_release_versions_keep_python_baseline_and_upgrade_new_surfaces(self) -> None:
        release = json.loads((ROOT / "release-metadata.json").read_text())

        self.assertEqual(release["python_baseline_version"], "0.1.0")
        self.assertEqual(release["release_version"], "0.2.0")
        self.assertEqual(release["git_tag"], "v0.2.0")
        self.assertEqual(release["license"], "MIT")

    def test_active_surface_manifest_has_twenty_two_logical_surfaces(self) -> None:
        manifest = json.loads((ROOT / "surface-manifest.json").read_text())

        self.assertEqual(len(manifest["surfaces"]), 22)
        self.assertEqual(
            {
                surface["version"]
                for surface in manifest["surfaces"]
                if surface["active"] and surface["id"] != "python-baseline"
            },
            {"0.2.0"},
        )
        self.assertNotIn("hex.pm", json.dumps(manifest).lower())
        self.assertNotIn("hexdocs", json.dumps(manifest).lower())
        self.assertNotIn("chocolatey", json.dumps(manifest).lower())

    def test_every_active_surface_declares_required_local_artifacts(self) -> None:
        manifest = json.loads((ROOT / "surface-manifest.json").read_text())

        for surface in manifest["surfaces"]:
            if not surface["active"]:
                continue
            with self.subTest(surface=surface["id"]):
                surface_root = ROOT / surface["path"]
                for relative_path in surface["required_files"]:
                    self.assertTrue(
                        (surface_root / relative_path).is_file(),
                        f"missing {surface['id']}/{relative_path}",
                    )

    def test_every_active_surface_has_nonempty_docs_metadata_source_test_and_dry_run(self) -> None:
        manifest = json.loads((ROOT / "surface-manifest.json").read_text())

        for surface in manifest["surfaces"]:
            if not surface["active"]:
                continue
            with self.subTest(surface=surface["id"]):
                surface_root = ROOT / surface["path"]
                for relative_path in ("README.md", "LICENSE", "surface.json", "dry-run.sh"):
                    artifact = surface_root / relative_path
                    self.assertTrue(artifact.is_file(), f"missing {surface['id']}/{relative_path}")
                    self.assertTrue(artifact.read_text().strip(), f"empty {surface['id']}/{relative_path}")
                for source_file in surface["source_files"]:
                    source = ROOT / source_file
                    self.assertTrue(source.is_file(), f"missing source {source_file}")
                    self.assertTrue(source.read_text().strip(), f"empty source {source_file}")

    def test_active_surface_readmes_include_target_and_usage_facts(self) -> None:
        manifest = json.loads((ROOT / "surface-manifest.json").read_text())

        for surface in manifest["surfaces"]:
            if not surface["active"]:
                continue
            with self.subTest(surface=surface["id"]):
                readme = (ROOT / surface["path"] / "README.md").read_text()
                self.assertIn("https://cleanpasteai.com/", readme)
                self.assertIn("normalizePastedText", readme)

    def test_index_surfaces_have_explicit_metadata_without_fake_duplicate_packages(self) -> None:
        manifest = json.loads((ROOT / "surface-manifest.json").read_text())
        expected = {
            "pkg-go-dev": "pkg.go.dev",
            "docs-rs": "docs.rs",
            "swift-package-index": "Swift Package Index",
        }

        for surface in manifest["surfaces"]:
            if surface["id"] not in expected:
                continue
            with self.subTest(surface=surface["id"]):
                metadata = json.loads((ROOT / surface["path"] / "metadata.json").read_text())
                self.assertEqual(metadata["index"], expected[surface["id"]])
                self.assertEqual(metadata["version"], "0.2.0")
                self.assertEqual(metadata["homepage"], "https://cleanpasteai.com/")
                self.assertTrue(metadata["source_file"])

    def test_registry_surfaces_have_scoped_registry_metadata(self) -> None:
        github = json.loads((ROOT / "surfaces/github-packages/registry-metadata.json").read_text())
        self.assertEqual(github["scope"], "@bbwdadfg")
        self.assertEqual(github["registry"], "https://npm.pkg.github.com/")
        self.assertEqual(github["version"], "0.2.0")
        self.assertTrue(github["token_required"])

        gitlab = json.loads((ROOT / "surfaces/gitlab-package/registry-metadata.json").read_text())
        self.assertEqual(gitlab["scope"], "@bbwdadfg")
        self.assertEqual(
            gitlab["registry"],
            "https://gitlab.com/api/v4/projects/${CI_PROJECT_ID}/packages/npm/",
        )
        self.assertEqual(gitlab["project_id_env"], "CI_PROJECT_ID")
        self.assertTrue(gitlab["token_required"])

        github_package = json.loads((ROOT / "surfaces/github-packages/package.json").read_text())
        self.assertEqual(github_package["name"], "@bbwdadfg/cleanpaste-normalizer")
        self.assertEqual(github_package["publishConfig"]["registry"], "https://npm.pkg.github.com/")

        gitlab_package_text = (ROOT / "surfaces/gitlab-package/package.json").read_text()
        self.assertNotIn("PROJECT_ID", gitlab_package_text)
        gitlab_npmrc = (ROOT / "surfaces/gitlab-package/.npmrc.example").read_text()
        self.assertIn("@bbwdadfg:registry=https://gitlab.com/api/v4/projects/${CI_PROJECT_ID}/packages/npm/", gitlab_npmrc)

    def test_maven_pom_has_central_release_artifacts_and_signing_configuration(self) -> None:
        pom = (ROOT / "surfaces/maven/pom.xml").read_text()

        for required in (
            "<groupId>io.github.bbwdadfg</groupId>",
            "<artifactId>cleanpaste-normalizer</artifactId>",
            "<version>0.2.0</version>",
            "maven-source-plugin",
            "maven-javadoc-plugin",
            "maven-gpg-plugin",
            "central-publishing-maven-plugin",
            "<publishingServerId>central</publishingServerId>",
            "<autoPublish>false</autoPublish>",
        ):
            self.assertIn(required, pom)

    def test_root_manifest_and_dry_run_describe_the_release_without_changing_python_baseline(self) -> None:
        manifest = json.loads((ROOT / "surface-manifest.json").read_text())
        self.assertEqual(manifest["license"], "MIT")
        self.assertEqual(manifest["homepage"], "https://cleanpasteai.com/")
        self.assertEqual(manifest["repository"], "https://cleanpasteai.com/")
        self.assertEqual(manifest["source"], "https://cleanpasteai.com/")
        self.assertEqual(manifest["release_version"], "0.2.0")
        self.assertEqual(manifest["git_tag"], "v0.2.0")
        baseline = next(surface for surface in manifest["surfaces"] if surface["id"] == "python-baseline")
        self.assertEqual(baseline["version"], "0.1.0")
        self.assertIn("dry-run.sh", baseline["required_files"])
        self.assertTrue((ROOT / "future-candidates/chocolatey.json").is_file())
        chocolatey = json.loads((ROOT / "future-candidates/chocolatey.json").read_text())
        self.assertFalse(chocolatey["active"])

    def test_all_new_surface_metadata_points_to_cleanpasteai(self) -> None:
        manifest = json.loads((ROOT / "surface-manifest.json").read_text())

        for surface in manifest["surfaces"]:
            if not surface["active"] or surface["id"] == "python-baseline":
                continue
            with self.subTest(surface=surface["id"]):
                self.assertEqual(surface["version"], "0.2.0")
                self.assertEqual(surface["license"], "MIT")
                self.assertEqual(surface["homepage"], "https://cleanpasteai.com/")
                self.assertEqual(surface["repository"], "https://cleanpasteai.com/")
                self.assertEqual(surface["source"], "https://cleanpasteai.com/")


if __name__ == "__main__":
    unittest.main()
