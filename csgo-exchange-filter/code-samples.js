function get_items () {
    return $('.inventory_item');
}

function filter_items (items, min_price, max_price) {
    var result = [];
    for (var i=0; i<items.length; i++) {
        var item = items[i]
        var price = parseInt($(items[i]).find('.item_price span').text());
        if (price >= 11 && price <= 45) {
            result.push(item)
        }
    }
    return result;
}

/**
 * TODO
 * Version A:
 * - Add tab for "Tasty" stuff
 * - Periodically query bots via AJAX
 * - Filter returned stuff and draw it there
 * Version B:
 * - just kill all unneccessary shit 
 */

// version 2 helper

function kill_infidels (min_price, max_price) {
    var items = $('.inventory_item');
    for (var i = 0; i < items.length; i ++) {
        var item = items[i]
        var price = parseInt($(items[i]).find('.item_price span').text());
        if (price < min_price || price > max_price) {
            item.remove();
        }
    }
}

MIN_PRICE = 11;
MAX_PRICE = 45;

stop_me = setInterval(function () {
    console.log('cleared', kill_infidels(MIN_PRICE, MAX_PRICE));
}, 2000);
