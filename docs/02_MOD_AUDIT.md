# Mod 衝突審查表（初始待檢）

| 模組／工具 | 目前定位 | 可能衝突點 | 下一步 |
|---|---|---|---|
| RPFM | 編輯/檢查 Pack，非遊戲 Mod | 無遊戲載入衝突 | 核對實際版本與資料表 schema |
| Tiered Unit Size | 分級兵額機制參考，不直接整包複製 | 兵種模板、招募限制、AI、成本 | 逐 key 比較，確認授權與實際作用 |
| 1.7.2 Bug Fix | 基礎品質候選 | 與大型整合 Mod 重複修補 | 逐條確認，不假設永遠相容 |
| Better Garrison | 駐軍設計參考 | 駐軍表、建築、補員 | P0 後決定是否加入 |
| Lower Upkeep for Garrisoned Units | 成本方案參考 | upkeep/駐軍效果可能覆蓋新公式 | P2 自己重做，避免重疊 |
| More Generals and Units per Army | 延後的額外將領方案 | DLL、編制、戰場上限、版本 | 不納入第一版 |
| 戰役 `startpos` 修改 | 獨立開局包 | 多個劇本覆蓋同一 startpos | 每個開局單獨測試與發布 |

檢查方法：用 RPFM 同時開啟原版與候選 Mod，記錄資料表完整路徑與 row keys，衝突可能在 DB 同一列、Script 同一路徑、Startpos、DLL 或遊戲機制互斥。**「不同 Pack」不等於「必然相容」。**

不要將他人 Mod 的實際 `.pack`、程式碼或美術直接整合發布，除非作者授權允許。

工具說明：<https://frodo45127.github.io/rpfm/manual/packs/pack-operations.html>
