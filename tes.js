var Car = {
    jenis : "Toyota Yamaha",
    roda : 4,
    suara : function(){
        console.log("ngenggg")
    },
    penumpang : {
        "penumpang 1" : "Andi",
        penumpang2 : "Budi"
    }
}

console.log(Car.roda)
Car.roda += 4
Car.suara()
console.log(Car.penumpang["penumpang 1"])
console.log(Car.penumpang.penumpang2)