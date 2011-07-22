watch(/problem_\d\/solution.py$/) do |matches|
    system "clear && python #{matches[0]}"
end
