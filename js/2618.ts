function checkIfInstanceOf(obj: any, classFunction: any): boolean {
    if (obj == null || typeof classFunction !== "function") {
        return false;
    }

    return Object(obj) instanceof classFunction;
}

console.log(checkIfInstanceOf(new Date(), Date));
/**
 * checkIfInstanceOf(new Date(), Date); // true
 */

class Animal {}; class Dog extends Animal {}; console.log(checkIfInstanceOf(new Dog(), Animal));
console.log(checkIfInstanceOf(Date, Date))
console.log(checkIfInstanceOf(5, Number))
console.log(checkIfInstanceOf(5.9, Number))
console.log(checkIfInstanceOf("string", String))