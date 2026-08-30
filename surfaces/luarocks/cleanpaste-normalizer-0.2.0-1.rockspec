package = "cleanpaste-normalizer"
version = "0.2.0-1"
source = {
   url = "https://cleanpasteai.com/releases/cleanpaste-normalizer-0.2.0.tar.gz"
}
description = {
   summary = "Local pasted-text normalization helper.",
   homepage = "https://cleanpasteai.com/",
   license = "MIT"
}
build = {
   type = "builtin",
   modules = { cleanpaste_normalizer = "src/cleanpaste_normalizer.lua" }
}
