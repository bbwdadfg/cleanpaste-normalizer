local M = {}

local zero_width = {
  ["\226\128\139"] = "", ["\226\128\140"] = "", ["\226\128\141"] = "",
  ["\226\128\142"] = "", ["\226\128\143"] = "", ["\226\128\170"] = "",
  ["\226\128\171"] = "", ["\226\128\172"] = "", ["\226\128\173"] = "",
  ["\226\128\174"] = "", ["\226\129\160"] = "", ["\239\187\191"] = ""
}

local unicode_spaces = {
  ["\194\160"] = " ", ["\225\154\128"] = " ", ["\226\128\128"] = " ",
  ["\226\128\129"] = " ", ["\226\128\130"] = " ", ["\226\128\131"] = " ",
  ["\226\128\132"] = " ", ["\226\128\133"] = " ", ["\226\128\134"] = " ",
  ["\226\128\135"] = " ", ["\226\128\136"] = " ", ["\226\128\137"] = " ",
  ["\226\128\138"] = " ", ["\226\128\175"] = " ", ["\226\129\159"] = " ",
  ["\227\128\128"] = " "
}

local compatibility = { ["①"] = "1", ["Ａ"] = "A" }

local function replace_map(text, mapping)
  for from, to in pairs(mapping) do text = text:gsub(from, to) end
  return text
end

function M.normalize_pasted_text(text)
  assert(type(text) == "string", "text must be a string")
  text = text:gsub("\r\n", "\n"):gsub("\r", "\n")
  text = replace_map(text, compatibility)
  text = replace_map(text, zero_width)
  text = replace_map(text, unicode_spaces)
  text = text:gsub("[ \t]+\n", "\n")
  return text:gsub("[ \t]+$", "")
end

return M
