//Variables

// var b='somethings';
// var c=200;
// console.log(c);
// console.log(b);

// document.getElementById("SomeText").innerHTML='hey there';
// var age = prompt('What is your age');
// document.getElementById("SomeText").innerHTML=age+" is my age";


//Numbers  in javascript

var num1= 100;
console.log(num1);
num1=num1 +1000;
console.log(num1);


//functions

function fun1(){
    var x=prompt("What is your name?");
    var result="Hello " +x;
    console.log(result);
}
fun1();

var names='ronjacob';

console.log(names.length);
console.log(names.indexOf('jac'));
console.log(names.slice(2,5));
console.log(names.replace('ron','tom'));
console.log(names.toUpperCase());
console.log(names. charAt(2));
console.log(names[2]);
console.log(names.split(''));

var a=['ron','jacob','varghese'];
var b=new Array('Arya','R','N');

console.log("Conversion to string:",a.toString());
console.log(a.join(' '));
console.log(a.push('is an idiot'),a.join(' '));
console.log(a.pop()+" is deleted\n",a.join(' '));
b.shift();
console.log(b);
b.unshift('Arya');
console.log(b);
console.log(a.concat(b));
console.log(a.slice(1,2));
console.log(a.reverse());

console.log(a.sort())

no=[100,1,2,3,6,5]
console.log(no.sort(function(a,b){return a-b}));//ascending order
console.log(no.sort(function(a,b){return b-a}));//descending order









