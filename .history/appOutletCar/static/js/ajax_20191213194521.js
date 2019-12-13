$(document).ready(function(){
    $('section.pure > header.pricing-table-header > h2.pricing-table-price > a').each (function(){
        var href = $(this).attr("href");
        href = href.replace("post", "postAjax")
        $(this).qtip({
            content:{
                url: href,
                method:'get'
            }
        });
    });
   
});