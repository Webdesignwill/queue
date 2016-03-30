$(function () {

  "use strict";

  function joinQueue (e) {
    $(this).attr('disabled', 'disabled');
  }

  var $joinQueueBtn = $('#join-queue');
  $joinQueueBtn.on('mouseup', joinQueue);

});