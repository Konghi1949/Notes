### 开始
- node安装hexo
- 在目标文件夹下用`hexo init` 或者 `hexo init <folder>`构建项目，若无法使用，可以把github上的项目clone下来
- 进入folder使用`npm install`

### 根目录
| 文件/文件夹  | 作用                      |
| ------------ | ------------------------- |
| _config.yml  | 配置                      |
| package.json | app信息（node与hexo信息） |
| scaffolds    | 模板库                    |
| source       | 资源库                    |
| themes       | 主题                      |

### 配置(_config.yml)
网站：
| 参数        | 作用                |
| ----------- | ------------------- |
| title       | 网站标题            |
| subtitle    | 网站副标题          |
| description | 网站描述            |
| keywords    | 网站关键词          |
| author      | 作者                |
| language    | 语言(zh-Hans/zh-CH) |
| timeone     | 时区(Asic/Shanghai) |

网址：
| 参数                       | 作用                                 |
| -------------------------- | ------------------------------------ |
| url                        | http://或https://                    |
| root                       | 网站根目录                           |
| permalink                  | 文章的永久链接格式                   |
| permalink_defaults         | 永久链接中各部分的默认值             |
| pretty_urls                | 改写`permalink`的值来美化URL         |
| pretty_urls.trailing_index | 是否在永久链接中保留尾部的index.html |
| pretty_url.trailing_html   | 是否在永久链接中保留尾部的.html      |

目录：
| 参数         | 默认值         | 作用                                         |
| ------------ | -------------- | -------------------------------------------- |
| source_dir   | source         | 资源文件夹                                   |
| public_dir   | pubilc         | 公共文件夹，用于生成站点文件                 |
| tag_dir      | tags           | 标签文件夹                                   |
| archive_dir  | archives       | 归档文件夹                                   |
| category_dir | categories     | 分类文件夹                                   |
| code_dir     | downloads/code | Include code文件夹                           |
| 8n_dir       | :lang          | 国际化(i18n)文件夹                           |
| ip_render    |                | 跳过指定文件的渲染，使用glob表达式在匹配路径 |

文章：
| 参数                  | 作用                                         | 默认值    |
| --------------------- | -------------------------------------------- | --------- |
| new_post_name         | 新文章文件名                                 | :title.md |
| default_layout        | 预设布局                                     | post      |
| auto_spacing          | 中文与英文间加空格                           | false     |
| titlecase             | 将标题转换为title case                       | false     |
| external_link         | 在新标签中打开连接                           | true      |
| external_link.enable  | 在新标签中打开连接                           | true      |
| external_link.field   | 对整个网站（site）生效或只对文章（post）生效 | site      |
| external_link.exclude | 需要排除的域名                               | []        |
| filename_case         | 把文件名称转换为小写或大写(1/2)              | 0         |
| render_drafts         | 显示草稿                                     | false     |
| post_asset_folder     | 启动Asset文件夹                              | false     |
| relative_link         | 把链接改为以根目录的相对地址                 | false     |
| future                | 显示未来的文章                               | true      |
| highlight             | 代码块的设置                                 |           |
| presmjs               | -                                            |           |

分类与标签:
| 参数             | 作用     | 默认值        |
| ---------------- | -------- | ------------- |
| default_category | 默认分类 | uncategoriced |
| category_map     | 分类别名 |               |
| tag_map          | 标签别名 |               |

时间与日期格式：
| 参数           | 作用                                           | 默认值     |
| -------------- | ---------------------------------------------- | ---------- |
| date_format    | 日期格式                                       | YYYY-MM-DD |
| time_format    | 时间格式                                       | HH:mm:ss   |
| updated_option | 当Front Matter 中没有指定update时updated的取值 | mtime      |
