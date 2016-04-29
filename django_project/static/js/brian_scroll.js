// When the DOM is ready
$(function() {

    // Draw the peices
    // drawTriangle("a", [150, 0],     [0,  150],   [110, 150],  "rgba(255, 255, 255, 0.5)")
    // drawTriangle("b", [260, 110],   [0,  150],   [300, 150],  "rgba(255, 255, 255, 0.5)")
    // drawTriangle("c", [150, 0],     [105, 45],    [300, 150],  "rgba(255, 255, 255, 0.5)")


    // Init ScrollMagic Controller
    var controller = new ScrollMagic();

    // Create Animation for 0.5s
    var a_tween = TweenMax.fromTo("#a", 1, {css: { opacity: 0} }, {css: { opacity: 0.8} }, {yoyo: true, ease: Linear.easeNone });
    // Create the Scene and trigger when visible
    var a_scene = new ScrollScene({ triggerElement: 'main', offset: 400 }).setTween(a_tween).addTo(controller);

    // Create Animation for 0.5s
    var b_tween = TweenMax.fromTo("#b", 1, {css: { opacity: 0} }, {css: { opacity: 0.8} }, {yoyo: true, ease: Linear.easeNone });
    // Create the Scene and trigger when visible
    var b_scene = new ScrollScene({ triggerElement: 'main', offset: 800 }).setTween(b_tween).addTo(controller);

    // Create Animation for 0.5s
    var c_tween = TweenMax.fromTo("#c", 1, {css: { opacity: 0} }, {css: { opacity: 0.8} }, {yoyo: true, ease: Linear.easeNone });
    // Create the Scene and trigger when visible
    var c_scene = new ScrollScene({ triggerElement: 'main', offset: 1200 }).setTween(c_tween).addTo(controller);




    // Add debug indicators fixed on right side
    // a_scene.addIndicators();
    // b_scene.addIndicators();
    // c_scene.addIndicators();


    function drawTriangle(id, a, b, c, fill) {
        
        var canvas = document.getElementById(id);
        
        if ( canvas.getContext ) {
            var ctx = canvas.getContext('2d');

            ctx.beginPath();
            ctx.moveTo( a[0], a[1] );
            ctx.lineTo( b[0], b[1] );
            ctx.lineTo( c[0], c[1] );
            ctx.closePath();
            ctx.fillStyle = fill;
            ctx.fill();
            // ctx.stroke();
        }
    }
  
});