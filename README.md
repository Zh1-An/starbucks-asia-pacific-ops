# starbucks-asia-pacific · 订单接入应用日志切片

APAC 订单接入应用的日志切片，取自 2026-10-18 一次上游抖动后的重试与熔断恢复过程。
用于排查提交超时问题，附一个简单的日志行分类器。

## 目录

| 路径 | 说明 |
|---|---|
| `logs/starbucks-asia-pacific-app-20261018.log` | 20 行日志切片，含一次上游超时重试与熔断恢复 |
| `src/log_router.py` | 日志行分类器（stack / retry / error / warn / info） |

## 应用标识

`starbucks-asia-pacific`

该标识出现在日志文件名、每行 logger 标签 `[starbucks-asia-pacific]`、
部署路径 `/opt/app/starbucks-asia-pacific/`，以及 `log_router.py` 的
`APP_ID` / `APP_HOME` / `LOG_DIR` 常量与类名中。

## 关键信息

| 项 | 值 |
|---|---|
| 部署路径 | `/opt/app/starbucks-asia-pacific/conf/app.yaml` |
| 消费组 | `starbucks-asia-pacific-g1` |
| 上游地址 | `https://order-router.example.com/v3/commit` |
| 提交超时阈值 | 3000ms |

## 排查结论

上游 `order-router` 在 14:22 前后出现约 40 秒的响应劣化，客户端重试 3 次后触发熔断，
16 秒后半开恢复。该时段提交成功率从 99.7% 短暂降至 92.1%，无数据丢失。

## 使用

```bash
python src/log_router.py logs/starbucks-asia-pacific-app-20261018.log
```

## 维护

订单接入组
