# -*- coding: utf-8 -*-

import os
import time


DELAY_SECONDS = 0.8


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def show_array(numbers, i=None, j=None, sorted_start=None, step=0, message=""):
    clear_screen()
    print("冒泡排序动态演示")
    print("=" * 60)
    print(f"第 {step} 步: {message}\n")

    print("下标: ", end="")
    for index in range(len(numbers)):
        print(f"{index:^6}", end="")
    print()

    print("数值: ", end="")
    for value in numbers:
        print(f"{value:^6}", end="")
    print()

    print("标记: ", end="")
    for index in range(len(numbers)):
        if index == i:
            marker = "i"
        elif index == j:
            marker = "j"
        elif sorted_start is not None and index >= sorted_start:
            marker = "OK"
        else:
            marker = ""
        print(f"{marker:^6}", end="")
    print("\n")

    print("说明: 每一轮都会把当前未排序部分中最大的数冒泡到右侧。")
    print("OK 表示该位置已经排好序。")
    print("=" * 60)
    time.sleep(DELAY_SECONDS)


def bubble_sort(numbers):
    numbers = numbers[:]
    length = len(numbers)
    step = 1

    show_array(numbers, step=step, message="初始数组")
    step += 1

    for pass_index in range(length - 1):
        swapped = False
        sorted_start = length - pass_index

        for index in range(length - 1 - pass_index):
            next_index = index + 1
            show_array(
                numbers,
                i=index,
                j=next_index,
                sorted_start=sorted_start,
                step=step,
                message=f"比较 {numbers[index]} 和 {numbers[next_index]}",
            )
            step += 1

            if numbers[index] > numbers[next_index]:
                numbers[index], numbers[next_index] = numbers[next_index], numbers[index]
                swapped = True
                show_array(
                    numbers,
                    i=index,
                    j=next_index,
                    sorted_start=sorted_start,
                    step=step,
                    message="左边的数更大，交换两个元素",
                )
            else:
                show_array(
                    numbers,
                    i=index,
                    j=next_index,
                    sorted_start=sorted_start,
                    step=step,
                    message="顺序正确，不需要交换",
                )
            step += 1

        show_array(
            numbers,
            sorted_start=length - pass_index - 1,
            step=step,
            message=f"第 {pass_index + 1} 轮结束，最大值已到达本轮末尾",
        )
        step += 1

        if not swapped:
            show_array(
                numbers,
                sorted_start=0,
                step=step,
                message="本轮没有发生交换，数组已经有序，提前结束",
            )
            return numbers

    show_array(numbers, sorted_start=0, step=step, message="排序完成")
    return numbers


def read_numbers():
    raw = input("请输入一组整数，用空格分隔（直接回车使用示例数据）: ").strip()
    if not raw:
        return [8, 3, 5, 1, 9, 2, 6]
    return [int(item) for item in raw.split()]


def main():
    try:
        numbers = read_numbers()
    except ValueError:
        print("输入错误: 请输入整数，并用空格分隔。")
        return

    sorted_numbers = bubble_sort(numbers)
    print("\n原始数组:", numbers)
    print("排序结果:", sorted_numbers)


if __name__ == "__main__":
    main()
