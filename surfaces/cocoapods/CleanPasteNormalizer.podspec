Pod::Spec.new do |spec|
  spec.name = "CleanPasteNormalizer"
  spec.version = "0.2.0"
  spec.summary = "Local pasted-text normalization helper."
  spec.description = "Deterministic, local normalization for pasted text."
  spec.homepage = "https://cleanpasteai.com/"
  spec.license = { :type => "MIT", :file => "LICENSE" }
  spec.source = { :http => "https://cleanpasteai.com/releases/cleanpaste-normalizer-0.2.0.tar.gz" }
  spec.source_files = "Sources/CleanPasteNormalizer.swift"
  spec.swift_version = "5.7"
end
