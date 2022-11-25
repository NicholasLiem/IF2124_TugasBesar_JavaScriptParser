a = 0
try {
    while (a < 5){
        if (a == 4){
            break
        }
        a++
    }
    if (a == 4){
        throw ("sesuatu")
    }
}
catch({err}) {
    console.log("yah masuk error")
}
finally {
    console.log("hihi")
}



