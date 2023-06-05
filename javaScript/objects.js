function Person(fn, ln, age, eye) {
  this.firstName = fn;
  this.lastName = ln;
  this.age = age;
  this.eyeColour = eye;
  this.fullName = () => `${this.firstName} ${this.lastName}`
}

const me = new Person("Sam", "Betmouni", 53, "hazel")
const you = new Person("Samir", "Betmouni", 53, "hazel")

