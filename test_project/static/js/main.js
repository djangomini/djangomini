$(document).ready(function () {

  var toggle_sidebar_btn = $('[data-toggle="offcanvas"]');
  var page_sidebar = $('.row-offcanvas');
  var page_content = $('.row-offcanvas > .page-content');
  var page_navbar = $('body > .navbar:first');

  // open sidebar
  toggle_sidebar_btn.on('click', function (event) {
    if (show_sidebar()) {
      // don't follow link
      event.preventDefault();
      // need to prevent close sidebar by click outside sidebar
      event.stopPropagation();
      // scroll to top of page (to show full sidebar)
      $("body").scrollTop(0);
    }
  });

  // close sidebar on click outside it
  both(page_navbar, page_content).on('click', function (event) {
    // don't follow click actions when press outside opened sidebar
    if (close_sidebar()) {
      // don't follow actions on clicked element
      event.preventDefault();
      event.stopPropagation();
    }
  });


  /*
   * Return intersection between two jQuery selectors.
   */
  function both(selector1, selector2) {
    return selector1.add(selector2);
  }


  /*
   * Close sidebar.
   * Return true if sidebar was opened.
   */
  function close_sidebar() {
    if (page_sidebar.hasClass('active')) {
      page_sidebar.removeClass('active');
      // return page content to visible state
      page_content.css('opacity', '1.0');
      return true;
    }
    // sidebar already closed
    return false;
  }

  /*
   * Show sidebar.
   */
  function show_sidebar() {
    if (! page_sidebar.hasClass('active')) {
      page_sidebar.toggleClass('active');
      // make page content dimmed
      page_content.css('opacity', '0.3');
      return true;
    }
    return false;
  }

});