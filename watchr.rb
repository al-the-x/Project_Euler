watch(/problem_\d\/solution.py$/) do |matches|
    system "clear && time python #{matches[0]}"
end

watch(/problem_\d\/solution.php$/) do |matches|
    system "clear && time phpunit #{matches[0]}"
end
