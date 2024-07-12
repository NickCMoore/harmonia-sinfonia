document.addEventListener('DOMContentLoaded', function () {
    var unreadCount = document.getElementById('notificationBell').dataset.unreadCount;
    var notificationBell = document.getElementById('notificationBell');
    var unreadCountBadge = document.getElementById('unreadCount');

    if (unreadCount > 0) {
        notificationBell.classList.add('notification-bell');
        unreadCountBadge.style.display = 'block';
        unreadCountBadge.textContent = unreadCount;
    } else {
        notificationBell.classList.remove('notification-bell');
        unreadCountBadge.style.display = 'none';
    }
});
