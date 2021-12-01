fn main() {
let mut counter = 0;
let mut counter_2 = 20;
let mut a: Vec<u8> = vec![1,2,3,4];
let mut v: Vec<u8> = Vec::from([1,2,3,4]);

let x = &[1, 2, 3];
for n in a {
    println!("hola");
}

while counter<10 && counter_2 > 0{
    counter+=1;
    counter_2-=1;
    v.push(counter_2);
    println!("hola");
}

v.pop();

}