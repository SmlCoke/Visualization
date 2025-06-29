SmlCoke: 这种方法虽然可行，但是我如果关闭退出本地仓库和终端后，下一次再打开终端进行pull和push时，还需要重新设置吗？
以及是不是对于每一个仓库都要像这样git remote set-url origin git@github.com:SmlCoke/Visulization_Study.git设置一次？有没有更好的设置方法？

GitHub Copilot: 你的问题很典型，下面为你详细解答：

---

### 1. 远程地址设置是否需要每次都设置？

**不需要每次都设置。**  
只要你在某个仓库里用 `git remote set-url origin ...` 设置过一次，之后 pull/push 都会用你设置的 SSH 地址，**不用每次都重新设置**。

---

### 2. 每个仓库都要设置一次吗？

**是的，每个仓库都要单独设置。**  
因为远程地址是保存在每个仓库的 config 文件里的，不是全局配置。

---

### 3. 有没有更好的全局设置方法？

#### 方法一：新 clone 仓库时直接用 SSH 地址  
以后新 clone 仓库时，直接用 SSH 地址，比如：
```bash
git clone git@github.com:用户名/仓库名.git
```
这样就不用再改 remote 了。

#### 方法二：配置全局 GitHub URL 重写（推荐进阶用法）
你可以让 git 自动把所有 github.com 的 https 地址重写为 ssh 地址：

```bash
git config --global url."git@github.com:".insteadOf "https://github.com/"
```

这样你以后即使用 https 地址 clone，git 也会自动用 ssh 地址操作，无需每次手动设置。

---

### 总结

- 每个仓库只需设置一次 remote。
- 新仓库建议直接用 SSH 地址 clone。
- 想全局自动用 SSH，可用 `insteadOf` 配置。

如需撤销全局重写，可用：
```bash
git config --global --unset url."git@github.com:".insteadOf
```

如需进一步操作指引，请随时提问！

SmlCoke: 你的方法很好，现在请把你这次对话的主要信息整理为markdown文档格式，方便我复制和以后查询

GitHub Copilot: ```markdown
# GitHub 仓库拉取与 SSH 配置常见问题整理

## 1. 如何从 GitHub 拉取数据到本地

- **首次克隆仓库：**
  ```bash
  git clone <仓库地址>
  ```
  例如：
  ```bash
  git clone https://github.com/SmlCoke/Visulization_Study.git
  ```

- **已有本地仓库同步远程数据：**
  ```bash
  git pull
  ```

---

## 2. 常见网络问题及排查

- **HTTPS 连接失败常见原因：**
  - 网络环境（如校园网、公司网）屏蔽了 GitHub 的 443 端口
  - 本地防火墙或安全软件拦截
  - 代理设置异常
  - DNS 问题

- **排查建议：**
  1. 检查网络，尝试浏览器访问 https://github.com
  2. 使用 `curl -v https://github.com` 测试 443 端口
  3. 检查和清除代理设置
     ```bash
     git config --global --unset http.proxy
     git config --global --unset https.proxy
     ```
  4. 检查 hosts 文件和 DNS 设置
  5. 尝试更换网络或使用 VPN

---

## 3. SSH 方式拉取仓库

- **生成 SSH 密钥：**
  ```bash
  ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
  ```
- **将公钥内容添加到 GitHub 账户的 SSH keys**
- **用 SSH 地址克隆或拉取：**
  ```bash
  git clone git@github.com:SmlCoke/Visulization_Study.git
  ```
  或
  ```bash
  git pull git@github.com:SmlCoke/Visulization_Study.git
  ```

---

## 4. 为什么 `git clone` 能成功但 `git pull` 失败？

- `git clone` 用的是 SSH 地址，`git pull` 用的是 HTTPS 地址（origin 远程地址不同）。
- 解决方法：将本地仓库的远程地址改为 SSH 地址。
  ```bash
  git remote set-url origin git@github.com:SmlCoke/Visulization_Study.git
  ```

---

## 5. 合并时出现编辑器界面怎么办？

- 这是 Git 让你填写合并说明，直接保存并退出即可。
- **Vim 操作：**
  - 按 `Esc`
  - 输入 `:wq`
  - 回车

---

## 6. 远程地址设置相关问题

- **是否每次都要设置？**
  - 只需在每个仓库设置一次，之后 pull/push 都会用 SSH 地址。

- **每个仓库都要设置吗？**
  - 是的，每个仓库都要单独设置。

- **有没有全局自动用 SSH 的方法？**
  - 可以用如下命令全局重写 GitHub 地址为 SSH：
    ```bash
    git config --global url."git@github.com:".insteadOf "https://github.com/"
    ```
  - 这样以后即使用 https 地址 clone，git 也会自动用 ssh 地址操作。

- **撤销全局重写：**
    ```bash
    git config --global --unset url."git@github.com:".insteadOf
    ```

---

## 7. 建议

- 新仓库建议直接用 SSH 地址 clone。
- 遇到网络问题优先尝试 SSH 方式。
- 如需全局自动用 SSH，可用 `insteadOf` 配置。

---
