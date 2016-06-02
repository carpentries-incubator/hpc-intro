require "kramdown"
require "json" 

abort "No input file specified" if ARGV.length == 0
input_file = ARGV[0]
markdown = File.read(ARGV[0])
doc1 = Kramdown::Document.new(markdown)
tree = doc1.to_hash_a_s_t
puts JSON.pretty_generate(tree)
