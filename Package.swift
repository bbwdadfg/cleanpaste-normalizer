// swift-tools-version: 5.7
import PackageDescription

let package = Package(
    name: "CleanPasteNormalizer",
    platforms: [.macOS(.v12)],
    products: [.library(name: "CleanPasteNormalizer", targets: ["CleanPasteNormalizer"])],
    targets: [
        .target(name: "CleanPasteNormalizer"),
        .testTarget(name: "CleanPasteNormalizerTests", dependencies: ["CleanPasteNormalizer"])
    ]
)
