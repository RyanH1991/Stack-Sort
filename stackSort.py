function sortStack(stack) {
console.log("sortStack");
console.log(stack);
  // Write your code here.
// two recursive functions. sort, insert.
// sort takes it all the way down, then if top is lower, okay. if top higher, insert.
// insert: if top is lower, push and return. otherwise pop and insert again.
var top;
if(stack.length > 0) {
top = stack.pop();
console.log("sort top = " + top);
sortStack(stack);
}
else{
return stack;
}
  if(top >= stack[stack.length-1] || stack.length === 0){
stack.push(top);
console.log(stack);
return stack;
}
else if(top < stack[stack.length-1]){
insert(stack, top);
//stack.push(top);
console.log(stack);
return stack;
}


}

function insert(stack, top) {
console.log("insert");
console.log("insert top = " + top);
console.log(stack);
//top = stack.pop()
//console.log("insert top = " + top);
if(stack.length === 0){
stack.push(top);
return;
}
if(top >= stack[stack.length-1]){
stack.push(top);
console.log(stack);
return;
}
else if(top < stack[stack.length-1]){
var newTop = stack.pop();
insert(stack, top);
stack.push(newTop);
console.log(stack);
return;
}
}

// Do not edit the line below.
exports.sortStack = sortStack;
