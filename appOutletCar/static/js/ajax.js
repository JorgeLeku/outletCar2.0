$(document).ready(function(){
    $('section.pure > content >pricing-tables > pure-u-1 > pricing-table > pricing-table-header > pricing-table-price > h2').each (function(){
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