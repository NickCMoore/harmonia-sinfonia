document.addEventListener('DOMContentLoaded', function () {
    const bellIcon = document.getElementById('notificationBell');
    if (bellIcon) {
        const unreadCount = parseInt(bellIcon.getAttribute('data-unread-count')) || 0;
        const unreadBadge = document.getElementById('unreadCount');

        if (unreadCount > 0) {
            unreadBadge.textContent = unreadCount;
            unreadBadge.style.display = 'inline-block';
            bellIcon.classList.add('has-unread');
        } else {
            unreadBadge.style.display = 'none';
            bellIcon.classList.remove('has-unread');
        }
    }
});
