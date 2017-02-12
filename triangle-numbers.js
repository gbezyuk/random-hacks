// треугольные числа

/*

Задача: написать функцию triangle_number(n), которая возвращает n-е треугольное число.

Примеры:
triangle_number(0) == 0

triangle_number(1) == 1
1

triangle_number(2) == 3
1
2 3

triangle_number(3) == 6
1
2 3
4 5 6

triangle_number(4) == 10
1
2 3
4 5 6
7 8 9 10

triangle_number(5) == 15
1  
2  3
4  5  6
7  8  9  10
11 12 13 14 15

triangle_number(n) == triangle(n-1) + n

*/

function get_triangle_number (n) {
    console.log('CALLING get_triangle_number with n = ', n)
    if ( n <= 0) return 0;
    return get_triangle_number(n - 1) + n
}

function tabulate (f, x0, x1, dx) {
    for (var x = x0; x < x1; x = x + dx) {
        console.log(x, f(x))
    }
}

// by gbezyuk 2017.02.12

function draw_last_line (n) {
    var previous_triangle_number = get_triangle_number(n - 1)
    var this_triangle_number = get_triangle_number(n)
    var last_line = []
    for (var i = previous_triangle_number + 1; i <= this_triangle_number; i++) {
        last_line.push(i)
    }
    console.log.apply(console, last_line)
}

function draw_triangle (n) {
    if (n <= 0) {
        return
    }
    if (n == 1) {
        console.log(1)
    }
    else {
        draw_triangle(n - 1)
        draw_last_line(n)
    }
}

function t (n) { 
    return (n + 1) * n / 2
}

var cache = {
    "1":1,
    "2":3,
    "3":6,
    "4":10,
    "5":15,
    "6":21,
    "7":28,
    "8":36,
    "9":45,
    "10":55,
    "11":66,
    "12":78,
    "13":91,
    "14":105,
    "15":120,
    "16":136,
    "17":153,
    "18":171,
    "19":190,
    "20":210,
    "21":231
}

function get_triangle_number_memoized (n) {
    console.log('CALLING get_triangle_number_memoized with n = ', n)
    if (cache[n]) {
        console.log('FOUND IN CACHE')
        return cache[n];
    }
    if ( n <= 0) {
        console.log('<= 0')
        return 0;
    }
    else {
        console.log('BUT WE NEED TO GO DEEPER...')
        cache[n] = get_triangle_number_memoized(n - 1) + n
        return cache[n]
    }
}
