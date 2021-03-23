$(document).ready(function(){
    $('#about-us').hide();
    $('#security').hide();
    $('#prodRange').hide();
})

$('#showabout').click(function(){
    $('#about-us').siblings().hide(1000);
    $('#about-us').show(1000);
})
$('#showsecurity').click(function(){
    $('#security').siblings().hide(1000);
    $('#security').show(1000);
})
$('#showProdRange').click(function(){
    $('#prodRange').siblings().hide(1000);
    $('#prodRange').show(1000);
})
    
