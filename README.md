# starbucks-asia-pacific · 订单接入应用日志切片（合成样本）

> ## ⚠️ SYNTHETIC TEST DATA - not a real leak. All data is fabricated.
>
> 本仓库是**授权内部检测链路自测**所用的金丝雀样本，内容 100% 合成。
> **第三方（含泄露情报厂商）请勿采信、勿扩散、勿作为任何泄露证据引用。**
> 日志行中的主机名、路径、订单号、堆栈均为虚构；IP 段为 RFC 5737 文档段。

---

## 仓库用途

模拟「生产日志切片被误提交到公开仓库」这一**日志报文类**泄露形态。
此类内容常被忽视，但会暴露部署路径、内部服务命名、上游地址与版本信息，
在真实事件中足以支撑资产测绘，因此是监测链路必须覆盖的一类。

## 涉及的标识（合成）

```
starbucks-asia-pacific
```

| 文件 | 命中位置 |
|---|---|
| `logs/starbucks-asia-pacific-app-20261018.log` | 文件名、每行 logger 标签 `[starbucks-asia-pacific]`、部署路径 `/opt/app/starbucks-asia-pacific/` |
| `src/log_router.py` | 模块常量 `APP_ID` / `APP_HOME` / `LOG_DIR`、类名 `StarbucksAsiaPacificLogRouter` |

## 文件清单

| 路径 | 说明 |
|---|---|
| `logs/starbucks-asia-pacific-app-20261018.log` | 20 行日志切片，含一次上游超时重试与熔断恢复过程 |
| `src/log_router.py` | 日志行分类器（stack / retry / error / warn / info） |

## 日志中的可观察信号

| 信号 | 示例 |
|---|---|
| 部署路径 | `/opt/app/starbucks-asia-pacific/conf/app.yaml` |
| 消费组名 | `starbucks-asia-pacific-g1` |
| 上游地址 | `https://order-router.example.com/v3/commit`（保留域名） |
| 异常堆栈 | `com.synthetic.http.PooledClient`（虚构包名） |

## 保留期限

本仓库为临时样本，**发布后 14 天内删除**。请勿 fork、勿镜像、勿归档。

---

*SYNTHETIC TEST DATA - not a real leak. All data is fabricated.*
