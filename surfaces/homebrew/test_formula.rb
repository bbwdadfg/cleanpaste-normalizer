formula = File.read(File.expand_path("Formula/cleanpaste-normalizer.rb", __dir__))
raise "wrong version" unless formula.include?("version \"0.2.0\"")
raise "wrong homepage" unless formula.include?("homepage \"https://cleanpasteai.com/\"")
actual = IO.popen(["ruby", File.expand_path("bin/cleanpaste-normalizer", __dir__)], "r+") do |io|
  io.write("Ａ\u00a0B")
  io.close_write
  io.read
end
raise "wrong normalization" unless actual == "A B"
