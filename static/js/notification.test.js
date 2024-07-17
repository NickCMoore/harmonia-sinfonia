/**
 * @jest-environment jsdom
 */

require('./notification.js');

test('displays unread badge and adds class when there are unread notifications', () => {
    document.body.innerHTML = `
        <div id="notificationBell" data-unread-count="5"></div>
        <span id="unreadCount"></span>
    `;

    document.dispatchEvent(new Event('DOMContentLoaded'));

    const bellIcon = document.getElementById('notificationBell');
    const unreadBadge = document.getElementById('unreadCount');

    expect(unreadBadge.textContent).toBe('5');
    expect(unreadBadge.style.display).toBe('inline-block');
    expect(bellIcon.classList.contains('has-unread')).toBe(true);
});

test('hides unread badge and removes class when there are no unread notifications', () => {
    document.body.innerHTML = `
        <div id="notificationBell" data-unread-count="0"></div>
        <span id="unreadCount"></span>
    `;

    document.dispatchEvent(new Event('DOMContentLoaded'));

    const bellIcon = document.getElementById('notificationBell');
    const unreadBadge = document.getElementById('unreadCount');

    expect(unreadBadge.style.display).toBe('none');
    expect(bellIcon.classList.contains('has-unread')).toBe(false);
});
