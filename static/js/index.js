document.addEventListener('DOMContentLoaded', function () {
    var bell = document.getElementById('notificationBell');
    var unreadCount = document.getElementById('unreadCount');

    if (bell) {
        var count = bell.getAttribute('data-unread-count');
        if (count > 0) {
            unreadCount.textContent = count;
            unreadCount.style.display = 'inline-block';
        } else {
            unreadCount.style.display = 'none';
        }
    }
});
