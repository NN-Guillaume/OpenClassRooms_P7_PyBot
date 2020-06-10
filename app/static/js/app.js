$(document).ready(function() {

    function initMap(lat, lng) {
        let position  = {lat: lat, lng : lng};
        let map = $('.map').last().get(0);
        console.log(map);
        let goMap = new google.maps.Map(map, {scrollwheel: true, zoom: 8, center: position});
        let marker = new google.maps.Marker({position: position, map: goMap})
    }

    var button = document.getElementById("search");

            function gearLoad()
            {
                var loader = document.getElementById("loading");
                loader.style.display = "block";
                console.log("devrait afficher");
                setInterval(function(){ loader.style.display = "none"; }, 1500);

            }

    function formSubmit(callback) {
        $("form").on("submit", function(e){
            e.preventDefault();
            gearLoad();
            callback();
        });
    }

    formSubmit (function() {
        clearTimeout(1500);
    });

    function switcher() {
        document.getElementById("loading").style.display = "block";
    }

//--------------------------------------------------------------------------  F O R M  -----------------------------------------------------------------------

    $("form").submit(function (e) {

        gearLoad();

        formSubmit();
        $('#Datas').append('<div class= "col-sm-12"> <br> <div class="row"> <div class="map col-sm-4"> </div> <div class="col-sm-8"> <aside class="bot"> </aside> <aside class="wiki"> </aside> </div> </div> </div> </div>');
        var maps = $('.map').last();
        console.log(maps)
        var wiki = $('.wiki').last();
        var bot = $('.bot').last();

        e.preventDefault();
        let query = $("input").val();
        $.post('/api', {
            query : query
        }).done(function (reponse) {
            maps.show();
            initMap(parseFloat(reponse['lat']), parseFloat(reponse['lng']));
            wiki.text(reponse['summary']);
            console.log(reponse['answer']);
            bot.text(reponse['answer']);
            window.scrollTo(0,document.body.scrollHeight);
            testBot();
        })
    });

});
