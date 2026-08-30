Pod::Spec.new do |spec|
  spec.name = "CleanPasteNormalizer"
  spec.version = "0.2.0"
  spec.summary = "Local pasted-text normalization helper."
  spec.description = "Deterministic, local normalization for pasted text."
  spec.homepage = "https://cleanpasteai.com/"
  spec.author = { "CleanPaste AI" => "https://cleanpasteai.com/" }
  spec.license = { :type => "MIT", :file => "LICENSE" }
  spec.source = { :git => "https://github.com/bbwdadfg/cleanpaste-normalizer.git", :tag => "v0.2.0" }
  spec.source_files = "surfaces/cocoapods/Sources/CleanPasteNormalizer.swift"
  spec.swift_version = "5.7"
end
