# 證據筆記：台灣兩大查核來源的「機器可讀」現況（案例 F）

**驗證方法**：curl 原始 HTML（瀏覽器 UA）+ grep 結構化標記，2026-07-20 實測。不採信 WebFetch 摘要。

## 台灣事實查核中心（TFC，tfc-taiwan.org.tw）
- 站台：WordPress（google-sitemap-generator / wp-content）；伺服器端渲染、可爬。
- HTTP 200；首頁、查核文列表、**單篇查核文**皆有 1 個 `application/ld+json` 區塊。
- **關鍵：ClaimReview 命中 0、claimReviewed 命中 0。** 結構化標記只有通用型：`Article` / `WebPage` / `BreadcrumbList` / `Organization` / `Person` / `ImageObject` 等（WordPress 預設）。
- 實測單篇：`https://tfc-taiwan.org.tw/migration_article_103853_47/` → 同上，無 ClaimReview。
- **判讀**：TFC 的查核**以一般文章形式發布，未輸出 ClaimReview**。機器讀得到「一篇文章」，但**認不出這是「某主張 + 查核判定」的更正**——Google 查核功能、查核聚合器、以及愈來愈多以此為訊號的模型/答案引擎，無法把它辨識為 verdict。
- **caveat**：①ClaimReview 只是其中一種可讀性訊號，缺它不代表完全不可觸達（文章正文仍可被爬取/攝入）②單篇抽樣，但站台 schema 是統一模板，高度可能全站一致。

## Cofacts（cofacts.tw / cofacts.g0v.tw）
- curl（含瀏覽器 UA）皆 **HTTP 403**（Cloudflare + 前端 SPA），開放網頁對爬蟲不友善。
- **判讀**：Cofacts 走的是**開放資料庫 + GraphQL API + 聊天機器人**模式，資料在 API/bot，不在可爬的開放網頁；網頁層對 agent 可讀性低，且 SPA 通常無 ClaimReview。
- **未竟**：需改由其 GraphQL API / GitHub 開放資料確認資料結構與授權，再判斷「進不進得了主流模型/答案引擎」。留待協定書階段。

## 對研究的意義
這是案例 F 與整體論點的**具體、可驗證證據**：即使台灣**已經做完查核**，也常以「模型辨識不出是更正」的形式發布——正是「在自己網站做完還不夠」的實例。屬供給側可讀性缺口，非內容缺口。
