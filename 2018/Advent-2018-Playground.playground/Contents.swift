import Foundation

let filePath = "/Users/rodk/github/advent-of-code/2018/5/input.txt"

var inputs = ""


if let fileContents = try? String(contentsOfFile: filePath) {
    inputs = fileContents.components(separatedBy: "\n")[0]
}

print(inputs)

Array(inputs)

