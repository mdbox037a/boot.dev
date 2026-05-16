package main

import (
	"errors"
)

type customer struct {
	id      int
	balance float64
}

type transactionType string

const (
	transactionDeposit    transactionType = "deposit"
	transactionWithdrawal transactionType = "withdrawal"
)

type transaction struct {
	customerID      int
	amount          float64
	transactionType transactionType
}

func updateBalance(cx *customer, tx transaction) error {
	if tx.transactionType == transactionDeposit {
		cx.balance += tx.amount
		return nil
	}
	if tx.transactionType == transactionWithdrawal {
		if cx.balance-tx.amount < 0 {
			return errors.New("insufficient funds")
		}
		cx.balance -= tx.amount
		return nil
	}
	return errors.New("unknown transaction type")
}
