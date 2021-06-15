- 在添加新东西前的hexo配置  

      将需要上传至github的内容放在source文件夹，例如CNAME、favicon.ico、images等，这样在 hexo d 之后就不会被删除了
- 原理  

      `hexo g`是hexo在执行hexo generate时会在本地先把博客生成的一套静态站点放到public文件夹中
      `hexo d`将其复制到.deploy文件夹并上传
