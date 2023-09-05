data_path <- "./dataset/diem_thi.csv"
data <- read.csv(data_path)
label <- c("KHXH", "KHTN", "Bỏ thi", "Bỏ thi khối")
quantity <- c(683813, 329430, 4476, 2170)
q1 <- data.frame(label, quantity)
library(ggplot2)
# Plot
ggplot(q1, aes(x=label, y=quantity)) +
  geom_point() + 
  geom_segment(aes(x=label, xend=label, y=0, yend=quantity))