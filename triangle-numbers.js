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

triangle_number(n) == triangle(n-1) + n

*/

function get_triangle_number (n) {
    if ( n == 0) return 0;
    return get_triangle_number(n - 1) + n
}

function tabulate (f, x0, x1, dx) {
    for (var x = x0; x < x1; x = x + dx) {
        console.log(x, f(x))
    }
}

function draw_triangle (n) {
    if (n == 0) {
        return 
    }
    if (n == 1) {
        console.log(1)
    }
    else {
        draw_triangle(n - 1)
        var previous_triangle_number = get_triangle_number(n - 1)
        var this_triangle_number = get_triangle_number(n)
        var last_line = []
        for (var i = previous_triangle_number + 1; i <= this_triangle_number; i++) {
            last_line.push(i)
        }
        console.log.apply(console, last_line)
    }
}