package main

type Analytics struct {
	MessagesTotal     int
	MessagesFailed    int
	MessagesSucceeded int
}

type Message struct {
	Recipient string
	Success   bool
}

func analyzeMessage(data *Analytics, msg Message) {
	if msg.Success {
		data.MessagesTotal++
		data.MessagesSucceeded++
	}
	if !msg.Success {
		data.MessagesTotal++
		data.MessagesFailed++
	}
}
