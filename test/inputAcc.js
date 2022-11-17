function do_something(x) {
    if (x == 4) {
      return +9;
    } else if (x + 4 == 1) {
      if (true) {
        return 3;
      } else {
        return 2;
      }
    } else if (x == 32) {
      return 4;
    } else {
      return "Momen"
    }
}

var a = do_something(4)

console.log(a)