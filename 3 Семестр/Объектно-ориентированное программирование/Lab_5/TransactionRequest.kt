class TransactionRequest(val amount: Double, val senderAccount: Account) {
    val bankLimit: Double = senderAccount.bank.limitForSuspiciousAccounts
}