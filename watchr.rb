watch(/.*\/solution\.\w+$/) do |matches|
    system "clear && time #{matches[0]}"
end

