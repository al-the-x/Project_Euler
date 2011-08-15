watch(/.*\/solution\.\w+$/) do |matches|
    system "chmod +x #{matches[0]}"
    system "clear && time #{matches[0]}"
end

