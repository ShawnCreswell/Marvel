jQuery(document).ready(function($){

    $('.live-search-list li').each(function(){
    $(this).attr('data-search-term', $(this).text().toLowerCase());
    });
    
    $('.live-search-box').on('keyup', function(){
    
    var searchTerm = $(this).val().toLowerCase();
    
        $('.live-search-list li').each(function(){
    
            if ($(this).filter('[data-search-term *= ' + searchTerm + ']').length > 0 || searchTerm.length < 1) {
                $(this).show();
            } else {
                $(this).hide();
            }
    
        });
    
    });
    
    });


    fetch("https://youtube.googleapis.com/youtube/v3/search?part=snippet&order=viewCount&q=hulk&key=AIzaSyDmNcGpYoh7kWzRRdoNFY8C9xQS4V1sIyk")
    .then((data)=>{
        console.log(data)
    })