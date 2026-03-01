// 现代化登录页面JavaScript
document.addEventListener('DOMContentLoaded', function() {
    // 初始化页面
    initializePage();
    
    // 绑定事件监听器
    bindEventListeners();
    
    // 初始化表单验证
    initializeFormValidation();
});

// 页面初始化
function initializePage() {
    // 添加页面加载动画
    document.body.style.opacity = '0';
    setTimeout(() => {
        document.body.style.transition = 'opacity 0.5s ease';
        document.body.style.opacity = '1';
    }, 100);
    
    // 设置当前日期
    updateDateTime();
    setInterval(updateDateTime, 1000);
}

// 绑定事件监听器
function bindEventListeners() {
    // 登录表单提交
    const loginForm = document.getElementById('loginForm');
    if (loginForm) {
        loginForm.addEventListener('submit', handleLoginSubmit);
    }
    
    // 注册表单提交
    const registerForm = document.getElementById('registerForm');
    if (registerForm) {
        registerForm.addEventListener('submit', handleRegisterSubmit);
    }
    
    // 输入框焦点事件
    const inputs = document.querySelectorAll('input');
    inputs.forEach(input => {
        input.addEventListener('focus', handleInputFocus);
        input.addEventListener('blur', handleInputBlur);
        input.addEventListener('input', handleInputChange);
    });
    
    // 模态框外部点击关闭
    window.addEventListener('click', handleModalOutsideClick);
    
    // 键盘事件
    document.addEventListener('keydown', handleKeyboardEvents);
}

// 表单验证初始化
function initializeFormValidation() {
    // 实时验证
    const accountInput = document.getElementById('account');
    const passwordInput = document.getElementById('password');
    const regNameInput = document.getElementById('reg-name');
    const regPasswordInput = document.getElementById('reg-password');
    const confirmPasswordInput = document.getElementById('confirm-password');
    
    if (accountInput) {
        accountInput.addEventListener('input', () => validateAccount(accountInput));
    }
    
    if (passwordInput) {
        passwordInput.addEventListener('input', () => validatePassword(passwordInput));
    }
    
    if (regNameInput) {
        regNameInput.addEventListener('input', () => validateName(regNameInput));
    }
    
    if (regPasswordInput) {
        regPasswordInput.addEventListener('input', () => validateRegPassword(regPasswordInput));
    }
    
    if (confirmPasswordInput) {
        confirmPasswordInput.addEventListener('input', () => validateConfirmPassword(confirmPasswordInput));
    }
}

// 登录表单提交处理
function handleLoginSubmit(event) {
    event.preventDefault();
    
    const form = event.target;
    const submitBtn = form.querySelector('.login-btn');
    const account = form.querySelector('#account').value.trim();
    const password = form.querySelector('#password').value.trim();
    
    // 验证表单
    if (!validateLoginForm(account, password)) {
        return;
    }
    
    // 显示加载状态
    setButtonLoading(submitBtn, true);
    
    // 模拟登录请求
    setTimeout(() => {
        // 这里应该是实际的登录逻辑
        form.submit();
    }, 1000);
}

// 注册表单提交处理
function handleRegisterSubmit(event) {
    event.preventDefault();

    const form = event.target;
    const submitBtn = form.querySelector('.register-submit-btn');
    const name = form.querySelector('#reg-name').value.trim();
    const password = form.querySelector('#reg-password').value.trim();
    const confirmPassword = form.querySelector('#confirm-password').value.trim();

    // 验证表单
    if (!validateRegisterForm(name, password, confirmPassword)) {
        return;
    }

    // 显示加载状态
    setButtonLoading(submitBtn, true);

    // 添加确认密码字段到表单数据
    const confirmInput = document.createElement('input');
    confirmInput.type = 'hidden';
    confirmInput.name = 'confirm_password';
    confirmInput.value = confirmPassword;
    form.appendChild(confirmInput);

    // 提交表单
    setTimeout(() => {
        form.submit();
    }, 800);
}

// 输入框焦点处理
function handleInputFocus(event) {
    const wrapper = event.target.closest('.input-wrapper');
    if (wrapper) {
        wrapper.classList.add('focused');
    }
}

function handleInputBlur(event) {
    const wrapper = event.target.closest('.input-wrapper');
    if (wrapper) {
        wrapper.classList.remove('focused');
    }
}

function handleInputChange(event) {
    const input = event.target;
    const wrapper = input.closest('.input-wrapper');
    
    if (wrapper) {
        if (input.value.trim()) {
            wrapper.classList.add('has-value');
        } else {
            wrapper.classList.remove('has-value');
        }
    }
}

// 键盘事件处理
function handleKeyboardEvents(event) {
    // ESC键关闭模态框
    if (event.key === 'Escape') {
        closeRegisterModal();
    }
    
    // Enter键提交表单
    if (event.key === 'Enter') {
        const activeElement = document.activeElement;
        if (activeElement && activeElement.tagName === 'INPUT') {
            const form = activeElement.closest('form');
            if (form) {
                const submitBtn = form.querySelector('button[type="submit"]');
                if (submitBtn) {
                    submitBtn.click();
                }
            }
        }
    }
}

// 模态框外部点击处理
function handleModalOutsideClick(event) {
    const modal = document.getElementById('registerModal');
    if (event.target === modal) {
        closeRegisterModal();
    }
}

// 显示注册模态框
function showRegisterModal() {
    const modal = document.getElementById('registerModal');
    modal.style.display = 'block';
    
    // 聚焦到第一个输入框
    setTimeout(() => {
        const firstInput = modal.querySelector('input');
        if (firstInput) {
            firstInput.focus();
        }
    }, 300);
}

// 关闭注册模态框
function closeRegisterModal() {
    const modal = document.getElementById('registerModal');
    modal.style.display = 'none';

    // 重置表单
    const form = modal.querySelector('form');
    if (form) {
        form.reset();
        clearFormValidation(form);

        // 重置按钮状态
        const submitBtn = form.querySelector('.register-submit-btn');
        if (submitBtn) {
            setButtonLoading(submitBtn, false);
        }

        // 移除动态添加的确认密码字段
        const confirmInput = form.querySelector('input[name="confirm_password"][type="hidden"]');
        if (confirmInput) {
            confirmInput.remove();
        }
    }
}

// 密码显示/隐藏切换
function togglePassword() {
    const passwordInput = document.getElementById('password');
    const toggleBtn = passwordInput.nextElementSibling;
    
    if (passwordInput.type === 'password') {
        passwordInput.type = 'text';
        toggleBtn.textContent = '🙈';
    } else {
        passwordInput.type = 'password';
        toggleBtn.textContent = '👁️';
    }
}

// 表单验证函数
function validateLoginForm(account, password) {
    let isValid = true;
    
    if (!account) {
        showFieldError('account', '请输入账号');
        isValid = false;
    } else if (account.length < 2) {
        showFieldError('account', '账号长度至少2个字符');
        isValid = false;
    } else {
        clearFieldError('account');
    }
    
    if (!password) {
        showFieldError('password', '请输入密码');
        isValid = false;
    } else if (password.length < 6) {
        showFieldError('password', '密码长度至少6个字符');
        isValid = false;
    } else {
        clearFieldError('password');
    }
    
    return isValid;
}

function validateRegisterForm(name, password, confirmPassword) {
    let isValid = true;
    
    if (!name) {
        showFieldError('reg-name', '请输入姓名');
        isValid = false;
    } else if (name.length < 2) {
        showFieldError('reg-name', '姓名长度至少2个字符');
        isValid = false;
    } else {
        clearFieldError('reg-name');
    }
    
    if (!password) {
        showFieldError('reg-password', '请设置密码');
        isValid = false;
    } else if (password.length < 6) {
        showFieldError('reg-password', '密码长度至少6个字符');
        isValid = false;
    } else {
        clearFieldError('reg-password');
    }
    
    if (!confirmPassword) {
        showFieldError('confirm-password', '请确认密码');
        isValid = false;
    } else if (password !== confirmPassword) {
        showFieldError('confirm-password', '两次输入的密码不一致');
        isValid = false;
    } else {
        clearFieldError('confirm-password');
    }
    
    return isValid;
}

// 单个字段验证
function validateAccount(input) {
    const value = input.value.trim();
    if (!value) {
        setFieldState(input, 'error');
        return false;
    } else if (value.length < 2) {
        setFieldState(input, 'error');
        return false;
    } else {
        setFieldState(input, 'success');
        return true;
    }
}

function validatePassword(input) {
    const value = input.value.trim();
    if (!value) {
        setFieldState(input, 'error');
        return false;
    } else if (value.length < 6) {
        setFieldState(input, 'error');
        return false;
    } else {
        setFieldState(input, 'success');
        return true;
    }
}

function validateName(input) {
    const value = input.value.trim();
    if (!value) {
        setFieldState(input, 'error');
        return false;
    } else if (value.length < 2) {
        setFieldState(input, 'error');
        return false;
    } else {
        // 异步检查用户名可用性
        // change
        // checkUsernameAvailability(value, input);
        return true;
    }
}

// 检查用户名可用性
function checkUsernameAvailability(username, input) {
    // 防抖处理
    clearTimeout(input.checkTimeout);
    input.checkTimeout = setTimeout(() => {
        fetch(`/api/check-username/?username=${encodeURIComponent(username)}`)
            .then(response => response.json())
            .then(data => {
                if (data.available) {
                    setFieldState(input, 'success');
                    showFieldMessage(input, data.message, 'success');
                } else {
                    setFieldState(input, 'error');
                    showFieldMessage(input, data.message, 'error');
                }
            })
            .catch(error => {
                console.error('检查用户名时出错:', error);
                setFieldState(input, 'error');
                showFieldMessage(input, '检查用户名时出错', 'error');
            });
    }, 500); // 500ms防抖
}

function validateRegPassword(input) {
    const value = input.value.trim();
    if (!value) {
        setFieldState(input, 'error');
        return false;
    } else if (value.length < 6) {
        setFieldState(input, 'error');
        return false;
    } else {
        setFieldState(input, 'success');
        return true;
    }
}

function validateConfirmPassword(input) {
    const value = input.value.trim();
    const password = document.getElementById('reg-password').value.trim();
    
    if (!value) {
        setFieldState(input, 'error');
        return false;
    } else if (value !== password) {
        setFieldState(input, 'error');
        return false;
    } else {
        setFieldState(input, 'success');
        return true;
    }
}

// 字段状态设置
function setFieldState(input, state) {
    const wrapper = input.closest('.input-wrapper');
    if (wrapper) {
        wrapper.classList.remove('error', 'success');
        if (state) {
            wrapper.classList.add(state);
        }
    }
}

function showFieldError(fieldId, message) {
    const input = document.getElementById(fieldId);
    if (input) {
        setFieldState(input, 'error');
        showToast(message, 'error');
    }
}

function clearFieldError(fieldId) {
    const input = document.getElementById(fieldId);
    if (input) {
        setFieldState(input, 'success');
    }
}

function clearFormValidation(form) {
    const inputs = form.querySelectorAll('input');
    inputs.forEach(input => {
        setFieldState(input, null);
        clearFieldMessage(input);
    });
}

// 显示字段消息
function showFieldMessage(input, message, type) {
    clearFieldMessage(input);

    const wrapper = input.closest('.input-wrapper');
    if (wrapper) {
        const messageEl = document.createElement('div');
        messageEl.className = `field-message ${type}`;
        messageEl.textContent = message;
        wrapper.appendChild(messageEl);

        // 自动隐藏成功消息
        if (type === 'success') {
            setTimeout(() => {
                clearFieldMessage(input);
            }, 3000);
        }
    }
}

// 清除字段消息
function clearFieldMessage(input) {
    const wrapper = input.closest('.input-wrapper');
    if (wrapper) {
        const existingMessage = wrapper.querySelector('.field-message');
        if (existingMessage) {
            existingMessage.remove();
        }
    }
}

// 按钮加载状态
function setButtonLoading(button, loading) {
    if (loading) {
        button.classList.add('loading');
        button.disabled = true;
    } else {
        button.classList.remove('loading');
        button.disabled = false;
    }
}

// 提示消息
function showToast(message, type = 'info') {
    const toast = document.getElementById('toast');
    const toastMessage = toast.querySelector('.toast-message');
    const toastIcon = toast.querySelector('.toast-icon');
    
    // 设置消息内容
    toastMessage.textContent = message;
    
    // 设置图标和样式
    toast.className = 'toast ' + type;
    switch (type) {
        case 'error':
            toastIcon.textContent = '❌';
            break;
        case 'success':
            toastIcon.textContent = '✅';
            break;
        case 'warning':
            toastIcon.textContent = '⚠️';
            break;
        default:
            toastIcon.textContent = 'ℹ️';
    }
    
    // 显示提示
    toast.classList.add('show');
    
    // 自动隐藏
    setTimeout(() => {
        toast.classList.remove('show');
    }, 3000);
}

// 更新日期时间
function updateDateTime() {
    // 这里可以添加实时时间显示功能
    // 暂时不实现，保留接口
}

// 工具函数
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}
