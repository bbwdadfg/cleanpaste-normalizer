class CleanpasteNormalizer < Formula
  desc "Local pasted-text normalization helper"
  homepage "https://cleanpasteai.com/"
  url "https://github.com/bbwdadfg/cleanpaste-normalizer/archive/refs/tags/v0.2.0.tar.gz"
  version "0.2.0"
  sha256 "5a47a14a064db4d7609630c915c97760143f864e8eef439fdfea51e089222402"
  license "MIT"

  def install
    bin.install "bin/cleanpaste-normalizer"
  end

  test do
    assert_equal "A B", pipe_output("#{bin}/cleanpaste-normalizer", "Ａ\u00a0B")
  end
end
