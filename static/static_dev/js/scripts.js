$(document).ready(function(){
    var form = $('#form_buying_product');
    //console.log(form);
    form.on('submit', function (e) {

        // ... типа форма не отправляеться
        e.preventDefault();

        // печатаеть на консоль
        // console.log(123);

        var nmb = $('#number').val();
        console.log(nmb);

        var submit_btn = $('#submit_btn');
        var product_id = submit_btn.data("productId");
        var product_name = submit_btn.data("productName");
        var product_price = submit_btn.data("productPrice");

        // console.log(product_id);
        // console.log(product_name);
        // console.log(product_price);


        var data = {};
        data.product_id = product_id;
        data.nmb = nmb;

        var csrf_token = $('#form_buying_product [name="csrfmiddlewaretoken"]').val();
        data["csrfmiddlewaretoken"] = csrf_token;

        // Когда нужен будеть префиск какого-то языка.
        var url = form.attr("action");

        //console.log(data);

        $.ajax({
            url: url,
            type: 'POST',
            data: data,
            cache: true,
            success: function (data) {
                console.log("OK");
                console.log(data.products_total_nmb);
                if (data.products_total_nmb) {
                    $('#basket_total_nmb').text("(" + data.products_total_nmb + ")");
                }
            },
            error: function(){
                console.log("error");
            }
        });


        $('.basket-items ul').append('<li>' + product_name + ',' + nmb + 'шт. ' + 'по ' + product_price + ' руб ' +
                                    '<a class="delete-item" href="#">X</a>' + '</li>');

    });

    // without toggle
    function showingBasket() {
        $('.basket-items').removeClass('hidden');
    }

    //with toggle Class
    // function showingBasket() {
    //     $('.basket-items').toggleClass('hidden');
    // }


    $('.basket-container').on('click', function (e) {
        e.preventDefault();
        showingBasket();
    });

    $('.basket-container').mouseover(function () {
        showingBasket();
    });

    // without toggle Class
    // $('.basket-container').mouseout(function () {
    //     $('.basket-items').addClass('hidden');
    // });

    // with toggleClass
    // временно Закомментирую, чтобы корзина была всегда открытов, потом я добавлю ajax.
    // $('.basket-container').mouseout(function () {
    //     showingBasket();
    // });

    // удаляем из корзины.
    // closest - находить ближайший li родител, топо того :-)
    $(document).on('click', '.delete-item', function (e) {
        e.preventDefault();
        $(this).closest('li').remove();
     });

});
