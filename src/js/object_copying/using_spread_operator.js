//! copying using spread operator '...'
let original = {
    name: "John",
    details: {
        age: 30,
        hobbies: ["reading", "gaming"]
    }
};

let copy = { ...original };


//? changes in top-level structure
original.name = "not john"
console.log(original.name);// changing original will not affect the copy
console.log(copy.name);
//? changes in nested elements
// original.details.age = 35;
// original.details.hobbies.push("cooking");
// console.log(copy.details.age); // Output: 35, changes in original reflect in the shallow copy
// console.log(original.details.age); // Output: 35, changes in original reflect in the shallow copy
// console.log(copy.details.hobbies); // Output: ["reading", "gaming", "cooking"], changes in original reflect in the shallow copy
// console.log(original.details.hobbies); // Output: ["reading", "gaming", "cooking"], changes in original reflect in the shallow copy
