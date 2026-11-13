# 參考資料、驗證狀態與來源

此檔用來避免把猜測、網路轉載、作者需求與實測混在一起。

| 來源 | 內容 | 證據狀態 |
|---|---|---|
| 使用者在 2026-11-13 對話中提出的設計 | 名將強、弱將有兵力限制、前線調兵、平時維持費約半價且按補員付費 | U：本計畫需求，非全戰原有規則 |
| RPFM 官方網站 | 支援 Three Kingdoms、Pack、DB、Lua、依賴與診斷 | F：工具文件，已查閱 |
| RPFM 官方 Pack 操作手冊 | 新建、存檔、比較／合併 Pack | F：工具文件，已查閱 |
| Steam 社群 2025-06《modify a mod》討論 | `land_units_templates_tables` 的 `Num Composed Entities` 可改單位規模 | F：玩家操作回報，仍待本機核實 |
| Tiered Unit Size Workshop 專案 | 用不同單位版本設計分級兵額的先例 | H：作為方案參考，尚未審查內部表格 |
| 自訂補員費 Lua 結算 | 戰後補員結算與 `decrease_treasury` 的互動 | H：待核對 API 與實測，不能聲稱已完成 |

來源連結：

- RPFM：<https://frodo45127.github.io/rpfm/>
- Pack 操作：<https://frodo45127.github.io/rpfm/manual/packs/pack-operations.html>
- Three Kingdoms 單位人數社群討論：<https://steamcommunity.com/app/779340/discussions/0/604158712017376034/>
- Tiered Unit Size：<https://steamcommunity.com/sharedfiles/filedetails/?id=3553702147>

後續每份實測加上遊戲版本、檔案 SHA、Mod 清單、測試截圖與 PASS/FAIL，不要把程式碼編譯通過誤稱遊戲通過。
