function copyArrayAndManipulate(array, callback) {
    const output = []
    for (let index = 0; index < array.length; index++) {
        output.push(callback(array[index]))
    }
    return output
}
// or, more simply ..
function copyArrayAndManipulate(array, callback) {
    return array.map(callback);
}
// or
function copyArrayAndManipulate(array, callback) {
    const output = [];
    array.forEach(element => {
        output.push(callback(element));
    });
    return output;
}

function mulBy2(input) {
    return input * 2
}
const result = copyArrayAndManipulate([2, 3, 4], mulBy2)
console.log(result)