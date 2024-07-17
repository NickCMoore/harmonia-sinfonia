/**
 * @jest-environment jsdom
 */

document.body.innerHTML = `
    <div>
        <i id="notificationBell" data-unread-count="3"></i>
        <span id="unreadCount" class="badge bg-danger position-absolute top-0 start-100 translate-middle p-2 rounded-circle"></span>
    </div>
`;

require('./notification.js');


test('displays unread badge and adds class when there are unread notifications', () => {
    const bellIcon = document.getElementById('notificationBell');
    const unreadBadge = document.getElementById('unreadCount');

    expect(unreadBadge.textContent).toBe('3');
    expect(unreadBadge.style.display).toBe('inline-block');
    expect(bellIcon.classList.contains('has-unread')).toBe(true);
});

test('hides unread badge and removes class when there are no unread notifications', () => {
    const bellIcon = document.getElementById('notificationBell');
    bellIcon.setAttribute('data-unread-count', '0');

    document.dispatchEvent(new Event('DOMContentLoaded'));

    const unreadBadge = document.getElementById('unreadCount');

    expect(unreadBadge.style.display).toBe('none');
    expect(bellIcon.classList.contains('has-unread')).toBe(false);
});